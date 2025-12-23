(function () {
  function isEditorPage() {
    const body = document.body;
    if (!body) return false;
    return (
      body.classList.contains("endpoint-edit") ||
      body.classList.contains("endpoint-view") ||
      body.classList.contains("endpoint-_print")
    );
  }

  function enhanceSidebarNav() {
    if (!isEditorPage()) return;

    const mainNav = document.getElementById("main-nav");
    if (!mainNav) return;

    const container = document.querySelector(".app-main > .container");
    if (!container) return;

    const heading = container.querySelector("h1");
    if (!heading) return;

    const backLink = heading.nextElementSibling;
    if (!backLink || backLink.tagName !== "A") return;

    // Only use the candidate when it actually looks like the Back control.
    const backButton = backLink.querySelector("button");
    let backLabelSource = "";
    if (backButton && backButton.textContent) backLabelSource = backButton.textContent;
    else if (backLink.textContent) backLabelSource = backLink.textContent;
    const backLabel = backLabelSource.trim();
    if (!backLink.href || !backLabel) return;

    backLink.classList.add("app-go-back-inline");

    if (mainNav.querySelector("li.app-sidebar-back")) return;

    const li = document.createElement("li");
    li.className = "app-sidebar-back";
    li.setAttribute("role", "presentation");

    const a = document.createElement("a");
    a.className = "app-sidebar-back-link";
    a.href = backLink.href;
    a.textContent = backLabel;

    li.appendChild(a);
    mainNav.insertBefore(li, mainNav.firstChild);
  }

  function insertArticleMeta() {
    if (!isEditorPage()) return;

    const mainNav = document.getElementById("main-nav");
    if (!mainNav) return;

    if (mainNav.querySelector("li.app-sidebar-article")) return;

    const shortName = (document.body && document.body.dataset && document.body.dataset.articleShort) || "";
    const numericId = (document.body && document.body.dataset && document.body.dataset.articleId) || "";
    if (!shortName && !numericId) return;

    const li = document.createElement("li");
    li.className = "app-sidebar-article";
    li.setAttribute("role", "presentation");

    const wrap = document.createElement("div");
    wrap.className = "app-sidebar-article-wrap";

    const label = document.createElement("div");
    label.className = "app-sidebar-article-label";
    label.textContent = "Article";

    const primary = document.createElement("div");
    primary.className = "app-sidebar-article-primary";
    primary.textContent = shortName || `#${numericId}`;

    wrap.appendChild(label);
    wrap.appendChild(primary);

    if (shortName && numericId) {
      const secondary = document.createElement("div");
      secondary.className = "app-sidebar-article-secondary";
      secondary.textContent = `#${numericId}`;
      wrap.appendChild(secondary);
    }

    li.appendChild(wrap);

    const backItem = mainNav.querySelector("li.app-sidebar-back");
    if (backItem && backItem.nextSibling) {
      mainNav.insertBefore(li, backItem.nextSibling);
    } else if (backItem) {
      mainNav.appendChild(li);
    } else {
      mainNav.insertBefore(li, mainNav.firstChild);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      enhanceSidebarNav();
      insertArticleMeta();
    });
  } else {
    enhanceSidebarNav();
    insertArticleMeta();
  }
})();
