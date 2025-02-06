var validators = {};

validators["general"] = [];

validators["general"].push({
	name: "short",
	missing: "ID of the paper is missing."
});

validators["general"].push({
	name: "n_studies",
	missing: "Number of studies is missing."
});

validators["general"].push({
	name: "first_study",
	missing: "Description of the first study is missing."
});

validators["transparency"] = [];

validators["transparency"].push({
	name: "open_access",
	missing: 'Answer to "A. Open access" is missing.'
});

validators["transparency"].push({
	name: "preregistration",
	missing: 'Answer to "B. Pre-registration" is missing.'
});

validators["transparency"].push({
	name: "statement_of_availability",
	missing: 'Answer to "1. Statement of availability" is missing.'
});

validators["transparency"].push({
	name: "materials_availability",
	missing: 'Answer to "2. Materials availability" is missing.'
});

validators["transparency"].push({
	name: "data_availability",
	missing: 'Answer to "3. Data availability" is missing.'
});

validators["transparency"].push({
	name: "code_availability",
	missing: 'Answer to "4. Analysis code availability" is missing.'
});

validators["methods"] = [];
validators["methods"].push({
	name: "background1",
	missing: 'Answer to "1. Does the paper contain a description of the research problem?" is missing.'
});

validators["methods"].push({
	name: "background2",
	missing: 'Answer to "2. Does the paper contain a description of a theory or theoretical dispute that makes the research problem significant?" is missing.'
});

validators["methods"].push({
	name: "background3",
	missing: 'Answer to "3. Does the paper discuss state of the art (provide a description of previous scholarship on the topic)?" is missing.'
});

validators["methods"].push({
	name: "background4",
	missing: 'Answer to "4. Does the paper provide a clear rationale for the research problem in terms of a broader theory or previous empirical research?" is missing.'
});

validators["methods"].push({
	name: "goals1",
	missing: 'Answer to "1. Does the paper contain a statement of what the studies are expected to accomplish (aims, goals, objectives)?" is missing.'
});

validators["methods"].push({
	name: "goals2",
	missing: 'Answer to "2. Are any goals, aims or objectives expressed in terms of a hypothesis/prediction?"" is missing.'
});

validators["methods"].push({
	name: "goals3",
	missing: 'Answer to "3. Does the paper make it clear how the studies differ from previous scholarship?" is missing.'
});

validators["methods"].push({
	name: "conceptual1",
	missing: 'Answer to "1. Have any theoretical concepts been defined (characterized in terms of other theoretical constructs)?" is missing.'
});

validators["methods"].push({
	name: "conceptual2",
	missing: 'Answer to "2. Have all key theoretical concepts invoked in the hypotheses/predictions been defined (characterized in terms of other theoretical constructs)?" is missing.'
});

validators["methods"].push({
	name: "conceptual3",
	missing: 'Answer to "3. Have all conceptual variables in the selected study been linked to actual measures (observable variables)?" is missing.'
});

validators["methods"].push({
	name: "recruitment1",
	missing: 'Answer to "1. General method of recruitment was described (research panel, crowdsourcing platform [which?], announcement for students [program, year, etc.])." is missing.'
});

validators["methods"].push({
	name: "recruitment2",
	missing: 'Answer to "2. Prescreening criteria are adequately described (location, language, education, SES, etc.)." is missing.'
});

validators["methods"].push({
	name: "recruitment3",
	missing: 'Answer to "3. Specific dates when recruitment was conducted were provided." is missing.'
});

validators["methods"].push({
	name: "incentives",
	missing: 'Answer to "E. Incentives for participation" is missing.'
});

validators["methods"].push({
	name: "participants1",
	missing: 'Answer to "1. Age (mean, median, standard deviation, range)" is missing.'
});

validators["methods"].push({
	name: "participants2",
	missing: 'Answer to "2. Gender" is missing.'
});

validators["methods"].push({
	name: "participants3",
	missing: 'Answer to "3. Ethnicity/cultural background/first language (depending on the context of the study)" is missing.'
});

validators["methods"].push({
	name: "participants4",
	missing: 'Answer to "4. Education" is missing.'
});

validators["methods"].push({
	name: "participants5",
	missing: 'Answer to "5. Important topic-specific characteristics (e.g., if the study concerns intuitions of philosophers, then distribution of specializations should be described, etc.)" is missing.'
});

validators["methods"].push({
	name: "exclusion0",
	missing: 'Answer to "1. Is it clearly stated whether there were any exclusions post-hoc in the study?" is missing.'
});

validators["methods"].push({
	name: "exclusion1",
	missing: 'Answer to "2. If participants were excluded from analysis, does the paper specify general exclusion criteria employed?" is missing.'
});

validators["methods"].push({
	name: "exclusion2",
	missing: 'Answer to "3. Does the paper justify (explicitly or implicitly) employing a specific exclusion criterion?" is missing.'
});

validators["methods"].push({
	name: "exclumeasure1",
	missing: 'Answer to "1. If some of the participants were rejected because they did not meet the demographic criteria, were these criteria presented (e.g., nonnatives, extensive philosophical education)?" is missing.'
});

validators["methods"].push({
	name: "exclumeasure2",
	missing: 'Answer to "2. If attention and/or manipulation check was used, was it sufficiently described (exact formulation of the question that was used and its place in the set of stimuli given to participants, etc.)?" is missing.'
});

validators["methods"].push({
	name: "exclumeasure3",
	missing: 'Answer to "3. If used, were time-related constraints (minimum possible comprehension and response time) sufficiently described?" is missing.'
});

validators["methods"].push({
	name: "kindofstudy",
	missing: 'Answer to "I. Kind of study" is missing.'
});

validators["methods"].push({
	name: "statistical_analysis",
	missing: 'Answer to "J. Method of statistical analysis (computation by hand/specific program)" is missing.'
});

validators["methodsq"] = [];

validators["methodsq"].push({
	name: "qmeasure1",
	missing: 'Answer to "1. Description of tools used to display stimuli (paper/online survey software/tools/platforms - LimeSurvey, PsychoPy, Qualtrics, etc.)" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure2",
	missing: 'Answer to "2. Description of implements/equipment used for collecting answers (pen, pencil, mouse, keyboard, special controllers, touchscreen)" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure3",
	missing: 'Answer to "3. Description of the construction of materials / stimuli" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure4",
	missing: 'Answer to "4. Does the paper report the exact formulation of the probes used in the study (not in reported speech)?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure5",
	missing: 'Answer to "5. Completeness of stimuli description" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure6a",
	missing: 'Answer to "6a. Is it specified whether stimuli (vignettes) were presented together with the probes (questions) or separately?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure6b",
	missing: 'Answer to "6b. Is it specified in what order stimuli (vignettes) and probes (questions) were presented (or how this was randomized)?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure6c",
	missing: 'Answer to "6c. Is it specified how many probes were presented simultaneously (on one page/screen)?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure6d",
	missing: 'Answer to "6d. Is it clear whether participants were able to go back to previous vignettes or questions?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure6e",
	missing: 'Answer to "6e. Is it clear if all the questions in the questionnaire were mandatory and, if not, which ones were and which were not?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure6f",
	missing: 'Answer to "6f. Are technical measures taken to elicit specific behaviors from participants (time delay between questions etc.) adequately described?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure7a",
	missing: 'Answer to "If nominal scale was used, are exact formulations of categories specified?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure7b",
	missing: 'Answer to "7b. If Likert (or similar) scale was used, is a numerical range provided (e.g., 1 to 7, -3 to 3)?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure7c",
	missing: 'Answer to "7c. If Likert (or similar) scale was used with non-numerical anchors/labels (e.g., “Strongly agree”), is it clear how many points were named (e.g., all, anchors, midpoint) and how exactly the labels were formulated?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure7d",
	missing: 'Answer to "7d. Is it clear whether the scale was presented horizontally or diagonally?" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure8",
	missing: 'Answer to "8. Description of study instructions" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure9",
	missing: 'Answer to "9. Duration of the probes (e.g., how much time for each question? Time limit on completion of questionnaire? Average completion time of questionnaire?)" is missing.'
});

validators["methodsq"].push({
	name: "qmeasure10",
	missing: 'Answer to "10. Method of assignment to groups is described" is missing.'
});

validators["methodsn"] = [];

validators["methodsn"].push({
	name: "nqmeasure1",
	missing: 'Answer to "1. Description of data-collection setting (specific enough to permit replication – “university classroom” is not enough)" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure2",
	missing: 'Answer to "2. Dates of data collection" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure3",
	missing: 'Answer to "3. Times of day when data were collected" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure4",
	missing: 'Answer to "4. Duration of data-collection sessions" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure5",
	missing: 'Answer to "5. Method of assignment to groups" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure6",
	missing: 'Answer to "6. Description of stimuli" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure7",
	missing: 'Answer to "7. Completeness of stimuli description" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure8",
	missing: 'Answer to "8. Specification of software used to display stimuli, including the versions" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure9",
	missing: 'Answer to "9. Description of equipment used to display stimuli" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure10",
	missing: 'Answer to "10. Description of study instructions" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure11a",
	missing: 'Answer to "11a. Orally face-to-face/in writing/recording" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure11b",
	missing: 'Answer to "11b. By whom?" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure11c",
	missing: 'Answer to "11c. When?" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure11d",
	missing: 'Answer to "11d. Is it clear whether the instructions were repeated?" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure11e",
	missing: 'Answer to "11e. Description of comprehension checks" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure12",
	missing: 'Answer to "12. Description of each task (specific enough to permit replication)" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure13",
	missing: 'Answer to "13. Description of all tools/instruments/equipment used to collect data" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure14",
	missing: 'Answer to "14. Specification of all software used to collect data" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure15",
	missing: 'Answer to "15. Discussion of validity and reliability of psychometric tools" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure16",
	missing: 'Answer to "16. Description of inter-rater validity and rater reliability" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure17",
	missing: 'Answer to "17. Is it clear whether manipulation checks were used?" is missing.'
});

validators["methodsn"].push({
	name: "nqmeasure18 ",
	missing: 'Answer to "18. Are manipulation checks described?" is missing.'
});

validators["results"] = [];

validators["results"].push({
	name: "flow1",
	missing: 'Answer to "1. Number of participants" is missing.'
});

validators["results"].push({
	name: "flow2",
	missing: 'Answer to "2. A flowchart/figure/table of participant flow" is missing.'
});

validators["results"].push({
	name: "flow3",
	missing: 'Answer to "3. Method of sample size calculation (power analysis, etc.)" is missing.'
});

validators["results"].push({
	name: "descriptive1",
	missing: 'Answer to "1. Simple descriptive statistics" is missing.'
});

validators["results"].push({
	name: "descriptive2",
	missing: 'Answer to "2. Confidence intervals" is missing.'
});

validators["results"].push({
	name: "inferential1",
	missing: 'Answer to "1. For inferential statistical tests (e.g., t, F, and chi-square tests)" is missing.'
});

validators["results"].push({
	name: "inferential2",
	missing: 'Answer to "2. Reporting of p-values" is missing.'
});

validators["results"].push({
	name: "inferential3",
	missing: 'Answer to "3. Effect sizes" is missing.'
});

validators["conclusions"] = [];

validators["conclusions"].push({
	name: "interpretation",
	missing: 'Answer to "A. Interpretation of results" is missing.'
});

validators["conclusions"].push({
	name: "validity",
	missing: 'Answer to "Indicate the number of threats to construct validity or generalizability discussed in the paper" is missing.'
});


function Validate(validators, section_name) {
	var missing = [];
	const section = document.getElementById(section_name);
	for (field of validators) {
		try {
			var input = section.querySelector('input[name="' + field.name + '"]');
			if (input.type == "text" && input.value.trim() == "") {
				missing.push(field.missing);
			}
			else if (input.type == "number" && input.value.trim() == "") {
				missing.push(field.missing);
			}
			else if (input && input && input.type == "radio") {
				var radioGroup = section.querySelectorAll('input[name="' + field.name + '"]');
				var isAnyRadioChecked = Array.from(radioGroup).some(radio => radio.checked);
				if (!isAnyRadioChecked) {
					missing.push(field.missing);
				}
			}
		} catch {
			console.log(field.name)
		}
	}
	if (missing.length == 0) { missing.push("Everything is OK") };
	alert(missing.join("\n"));
}

var validate_button = document.getElementById("validate");
validate_button.onclick = function () {
	let section_name = document.querySelector('.tab-pane.active').id;
	Validate(validators[section_name], section_name)
}


