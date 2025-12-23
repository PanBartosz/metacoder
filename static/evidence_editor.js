(() => {
  const meta = document.getElementById("page-meta");
  if (!meta) return;

  const mode = meta.dataset.mode || "view";
  const articleId = meta.dataset.articleId || "unknown";
  const userId = meta.dataset.userId || "anon";

  const modalEl = document.getElementById("evidence-modal");
  const modalTitleEl = document.getElementById("evidence-modal-title");
  const modalDoneEl = document.getElementById("evidence-modal-done");
  const statusEl = document.getElementById("evidence-status");
  const viewerEl = document.getElementById("evidence-viewer");
  const draftBannerEl = document.getElementById("draft-banner");

  if (!modalEl || !modalTitleEl) return;

  const DRAFT_INDEX_KEY = `metacoder:drafts:${userId}:${articleId}:index`;
  const draftKey = (fieldId) => `metacoder:drafts:${userId}:${articleId}:${fieldId}`;

  let activeFieldId = null;
  let editor = null;
  let hasUnsavedChanges = false;
  let isSubmitting = false;
  let statusTimeoutId = null;
  let draftBannerVisible = false;

  const safeJsonParse = (raw) => {
    try {
      return JSON.parse(raw);
    } catch {
      return null;
    }
  };

  const stripHtml = (html) => {
    const tmp = document.createElement("div");
    tmp.innerHTML = html || "";
    return (tmp.textContent || tmp.innerText || "").replace(/\s+/g, " ").trim();
  };

  const truncate = (text, maxLen) => {
    if (!text) return "";
    if (text.length <= maxLen) return text;
    return `${text.slice(0, maxLen - 1)}…`;
  };

  const getDraftIndex = () => {
    const parsed = safeJsonParse(localStorage.getItem(DRAFT_INDEX_KEY));
    return Array.isArray(parsed) ? parsed : [];
  };

  const setDraftIndex = (items) => {
    localStorage.setItem(DRAFT_INDEX_KEY, JSON.stringify(items));
  };

  const addToDraftIndex = (fieldId) => {
    const index = new Set(getDraftIndex());
    index.add(fieldId);
    setDraftIndex(Array.from(index));
  };

  const removeFromDraftIndex = (fieldId) => {
    const index = new Set(getDraftIndex());
    index.delete(fieldId);
    setDraftIndex(Array.from(index));
  };

  const saveDraft = (fieldId, html) => {
    try {
      localStorage.setItem(
        draftKey(fieldId),
        JSON.stringify({ value: html || "", ts: Date.now() }),
      );
      addToDraftIndex(fieldId);
    } catch (e) {
      console.warn("Draft save failed:", e);
    }
  };

  const clearDraft = (fieldId) => {
    localStorage.removeItem(draftKey(fieldId));
    removeFromDraftIndex(fieldId);
  };

  const clearAllDrafts = () => {
    const index = getDraftIndex();
    for (const fieldId of index) localStorage.removeItem(draftKey(fieldId));
    localStorage.removeItem(DRAFT_INDEX_KEY);
  };

  const updatePreview = (fieldId, html) => {
    const previewEl = document.getElementById(`${fieldId}-preview`);
    if (!previewEl) return;
    const text = stripHtml(html);
    if (text) {
      previewEl.textContent = truncate(text, 140);
    } else {
      previewEl.innerHTML = '<span class="text-muted"><em>No evidence yet.</em></span>';
    }
  };

  const setStatus = (message) => {
    if (!statusEl) return;
    if (statusTimeoutId) window.clearTimeout(statusTimeoutId);
    statusEl.textContent = message || "";
    statusTimeoutId = window.setTimeout(() => {
      statusEl.textContent = "";
    }, 2000);
  };

  const getFieldTextarea = (fieldId) => document.getElementById(fieldId);

  const syncActiveFieldFromEditor = () => {
    if (!activeFieldId || !editor) return;
    if (editor.status && editor.status !== "ready") return;
    const textarea = getFieldTextarea(activeFieldId);
    if (!textarea) return;

    const html = editor.getData();
    textarea.value = html;
    updatePreview(activeFieldId, html);
    saveDraft(activeFieldId, html);
    hasUnsavedChanges = true;
    setStatus("Draft saved");
  };

  const ensureEditor = () => {
    if (mode !== "edit") return null;
    if (editor) return editor;
    if (!window.CKEDITOR) return null;
    editor = window.CKEDITOR.instances["evidence-editor"] || null;
    if (!editor) return null;

    const debouncedSync = (() => {
      let timeoutId = null;
      return () => {
        if (timeoutId) window.clearTimeout(timeoutId);
        timeoutId = window.setTimeout(() => syncActiveFieldFromEditor(), 350);
      };
    })();

    editor.on("change", debouncedSync);
    editor.on("instanceReady", () => {
      if (statusEl) statusEl.textContent = "";
    });
    return editor;
  };

  const showDraftBanner = (restoredCount) => {
    if (!draftBannerEl || draftBannerVisible) return;
    draftBannerVisible = true;
    draftBannerEl.style.display = "";
    draftBannerEl.innerHTML = `
      <strong>Draft restored.</strong>
      Restored ${restoredCount} unsaved draft(s) from this browser.
      They are not saved to the database until you click <strong>Save</strong>.
      <button type="button" class="btn btn-xs btn-danger" id="discard-drafts">Discard drafts</button>
    `;

    const discardButton = document.getElementById("discard-drafts");
    if (discardButton) {
      discardButton.addEventListener("click", () => {
        clearAllDrafts();
        window.location.reload();
      });
    }
  };

  const restoreDrafts = () => {
    const index = getDraftIndex();
    if (!index.length) return;

    let restoredCount = 0;
    for (const fieldId of index) {
      const textarea = getFieldTextarea(fieldId);
      if (!textarea) continue;

      const draft = safeJsonParse(localStorage.getItem(draftKey(fieldId)));
      if (!draft || typeof draft.value !== "string") {
        clearDraft(fieldId);
        continue;
      }

      if ((draft.value || "") === (textarea.value || "")) {
        clearDraft(fieldId);
        continue;
      }

      textarea.value = draft.value;
      updatePreview(fieldId, draft.value);
      restoredCount += 1;
    }

    if (restoredCount > 0) {
      hasUnsavedChanges = true;
      showDraftBanner(restoredCount);
    }
  };

  const openModal = () => {
    if (window.jQuery && window.jQuery.fn && window.jQuery.fn.modal) {
      window.jQuery(modalEl).modal("show");
      return;
    }
    modalEl.style.display = "block";
  };

  const closeModal = () => {
    if (window.jQuery && window.jQuery.fn && window.jQuery.fn.modal) {
      window.jQuery(modalEl).modal("hide");
      return;
    }
    modalEl.style.display = "none";
  };

  document.addEventListener("click", (event) => {
    const button = event.target.closest(".js-evidence-open");
    if (!button) return;

    const fieldId = button.dataset.evidenceField;
    if (!fieldId) return;

    activeFieldId = fieldId;
    modalTitleEl.textContent = button.dataset.evidenceTitle || "Evidence";

    const textarea = getFieldTextarea(fieldId);
    const html = textarea ? textarea.value || "" : "";

    if (mode === "edit") {
      const inst = ensureEditor();
      if (inst) {
        if (!inst.status || inst.status === "ready") {
          inst.setData(html);
        } else {
          const onReady = () => {
            inst.setData(html);
            inst.removeListener("instanceReady", onReady);
          };
          inst.on("instanceReady", onReady);
        }
      }
    } else if (viewerEl) {
      viewerEl.textContent = stripHtml(html);
    }

    openModal();
  });

  if (modalDoneEl) {
    modalDoneEl.addEventListener("click", () => closeModal());
  }

  if (window.jQuery && window.jQuery.fn && window.jQuery.fn.modal) {
    window.jQuery(modalEl).on("hide.bs.modal", () => {
      if (mode === "edit") syncActiveFieldFromEditor();
      activeFieldId = null;
      if (viewerEl) viewerEl.textContent = "";
    });

    window.jQuery(modalEl).on("shown.bs.modal", () => {
      if (mode !== "edit") return;
      const inst = ensureEditor();
      if (!inst) return;
      try {
        inst.resize("100%", 600);
        inst.focus();
      } catch {
        // ignore
      }
    });
  }

  const formEl = document.querySelector("form");
  if (formEl) {
    formEl.addEventListener("submit", () => {
      isSubmitting = true;
      if (mode === "edit") syncActiveFieldFromEditor();
      if (window.CKEDITOR && window.CKEDITOR.instances) {
        for (const instance of Object.values(window.CKEDITOR.instances)) {
          try {
            instance.updateElement();
          } catch {
            // ignore
          }
        }
      }
    });
  }

  window.addEventListener("beforeunload", (e) => {
    if (mode !== "edit") return;
    if (!hasUnsavedChanges || isSubmitting) return;
    e.preventDefault();
    e.returnValue = "";
  });

  const wiredInputDrafts = new Set();
  const wiredCkeditorDrafts = new Set();

  const wireInlineDraftAutosave = () => {
    const fields = document.querySelectorAll(".draft-autosave");
    for (const field of fields) {
      if (!field || !field.id) continue;
      const fieldId = field.id;
      if (wiredInputDrafts.has(fieldId)) continue;

      let timeoutId = null;
      field.addEventListener("input", () => {
        hasUnsavedChanges = true;
        if (timeoutId) window.clearTimeout(timeoutId);
        timeoutId = window.setTimeout(() => {
          saveDraft(fieldId, field.value || "");
        }, 350);
      });

      wiredInputDrafts.add(fieldId);
    }
  };

  const wireCkeditorDraftAutosave = () => {
    if (!window.CKEDITOR || !window.CKEDITOR.instances) return false;

    let wiredAny = false;
    const fields = document.querySelectorAll(".draft-autosave");
    for (const field of fields) {
      if (!field || !field.id) continue;
      const fieldId = field.id;
      if (wiredCkeditorDrafts.has(fieldId)) continue;

      const inst = window.CKEDITOR.instances[fieldId];
      if (!inst) continue;

      const debounced = (() => {
        let timeoutId = null;
        return () => {
          hasUnsavedChanges = true;
          if (timeoutId) window.clearTimeout(timeoutId);
          timeoutId = window.setTimeout(() => {
            try {
              saveDraft(fieldId, inst.getData() || "");
            } catch {
              // ignore
            }
          }, 350);
        };
      })();

      inst.on("change", debounced);
      wiredCkeditorDrafts.add(fieldId);
      wiredAny = true;
    }

    return wiredAny;
  };

  if (mode === "edit") {
    restoreDrafts();
    wireInlineDraftAutosave();
    // CKEditor instances are created later; keep trying briefly.
    let tries = 0;
    const timer = window.setInterval(() => {
      wireCkeditorDraftAutosave();
      tries += 1;
      if (tries >= 30) window.clearInterval(timer);
    }, 200);
  }
})();
