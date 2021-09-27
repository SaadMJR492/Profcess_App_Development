//FUNCTIONS

//function to check if to append
function checkToPut(dataField) {
	if (typeof dataField === "string") {
		return dataField;
	} else {
		return "";
	}
}

//getting the data
function appendFunction(formName) {
	let newData = [];
	let data = $("[name^=" + formName + "]");
	for (let i = 0; i < data.length; i++) {
		newData.push(data[i].value);
		data[i].value = "";
	}
	return newData;
}

//function to parsedata
function pJSON(value) {
	return (value != '') ? JSON.parse(value) : [];
}

//function to load old data
function initiator(djangoFormId, modalFormId, textFormId) {
	modalFormId.val(djangoFormId.val())
	textFormId.text(djangoFormId.val())
}

//function to update data
function update(djangoFormId, modalFormId, textFormId) {
	djangoFormId.val(modalFormId.val())
	textFormId.text(modalFormId.val());
}

//USER PROFILE
$(()=>{
	// UserProfile
	let profileIDs = [
		// [DjangoFormId, popUpModalName, textFormId
		['#id_first_name', '[name="profile[firstName]"]', '#profileFirstName'],
		['#id_last_name', '[name="profile[lastName]"]', '#profileLastName'],
		['#id_dob', '[name="profile[dob]"]', '#profileDob'],
		['#id_gender', '[name="profile[gender]"]', '#profileGender'],
		/*['#id_industry', '[name="profile[industry]"]', '#profileIndustry'],
		['#id_location', '[name="profile[location]"]', '#profileLocation'],
		['#id_current_position', '[name="profile[position]"]', '#profilePosition'],
		['#id_pheadline', '[name="profile[expert]"]', '#profileExpert'],
		['#id_contact_information', '[name="profile[contact]"]', '#profileContact']*/
	]
	profileIDs.map((item) => {
		initiator($(item[0]), $(item[1]), $(item[2]))
	})
	$('#editProfile button[type="submit"]').click(() => {
		profileIDs.map((item) => {
			update($(item[0]), $(item[1]), $(item[2]))
		})
	});

	// Brief
	let descriptionIDs = [
		['#id_description', '[name=briefDescription]', '#briefDescription'],
		['#id_location', '[name="Location"]', '#Location']
	];
	descriptionIDs.map((item) => {
		initiator($(item[0]), $(item[1]), $(item[2]))
	})
	$('#editBrief button[type="submit"]').click(() => {
		descriptionIDs.map((item) => {
			update($(item[0]), $(item[1]), $(item[2]))
		})
	});
	/*initiator($(descriptionIDs[0]), $(descriptionIDs[1]), $(descriptionIDs[2]));
	$('#editBrief button[type="submit"]').click(() => {
		update($(descriptionIDs[0]), $(descriptionIDs[1]), $(descriptionIDs[2]))
	});*/


	let skillIDs = ['#id_skill_info', '[name=Skill]', '#Skill'];
	initiator($(skillIDs[0]), $(skillIDs[1]), $(skillIDs[2]));
	$('#editSkill button[type="submit"]').click(() => {
		update($(skillIDs[0]), $(skillIDs[1]), $(skillIDs[2]))
	});
})

let contactIDs = [
		['#id_contact_information', '[name=contactInfo]', '#contactInfo'],
		['#id_mailid', '[name="mailId"]', '#mailId']
	];
	contactIDs.map((item) => {
		initiator($(item[0]), $(item[1]), $(item[2]))
	})
	$('#editContact button[type="submit"]').click(() => {
		contactIDs.map((item) => {
			update($(item[0]), $(item[1]), $(item[2]))
		})
	});

//COMPANY LOGIC
let companyData = [];
$(()=>{
	let countOfCompanyData = 0;
	let expEvent;
	let companyIDs = [
		['#id_experience_title', '[name="iExp[designation]"]'],
		['#id_company_name', '[name="iExp[cName]"]'],
		['#id_company_city', '[name="iExp[city]"]'],
		['#id_company_state', '[name="iExp[state]"]'],
		['#id_start_company', '[name="iExp[from]"]'],
		['#id_end_company', '[name="iExp[till]"]']
	]

	companyIDs.map((item) => {
		companyData.push(pJSON($(item[0]).val()))
	})

	//adding the data that already exists
	for (let i = 0; i < 5; i++) {
		if (checkToPut(companyData[0][i])) {
			$("#iExp").append(`
        <div class="row">
		      <div class="col">
            <h3>${companyData[0][i]}</h3>
            <h3>${companyData[1][i]}</h3>
            <h5>
              <span> ${companyData[4][i]} </span>
              <span> ${companyData[5][i]} </span>
            </h5>
            <h5>
	            <span>${companyData[2][i]}</span>
	            <span>${companyData[3][i]}</span>
	        </h5>
          </div>
          <div class="col-2 text-right">
              <span><button name='${i}' data-toggle="modal" data-target="#addCompanyDetails" class="iExpEdit btn btn-sm fa fa-edit"></button></span>
          </div>
        </div>
        <hr>
		`);
		}
	}

	$(document).on("click", ".iExpEdit", (event) => {
		expEvent = event.target.attributes.name.value;
		for(let i=0;i<6;i++) {
			$(companyIDs[i][1]).val(companyData[i][expEvent])
		}
	});

	$('#addCompanyDetails .modal-footer > button[type="button"]').click(() => {
		if ($("#cDesignation").val() === "") {
			$(`<span class="text-red">Must have title</span>`).insertAfter($("#cDesignation"));
		} else {
			let data = appendFunction("iExp");
			let textInfo = $("#iExp");
			if (expEvent != undefined) {
				whichChild = 1 + parseInt(expEvent) + parseInt(expEvent)
				child = "#iExp > div.row:nth-child("+ whichChild +")";
				textInfo = $(child);
				textInfo.html(`
					<div class="col">
						<h3>${data[0]}</h3>
						<h3>${data[1]}</h3>
						<h5><span> ${data[4]} </span> <span> ${data[5]} </span></h5>
						<h5><span> ${data[2]} </span> <span> ${data[3]} </span></h5>
					</div>
					<div class="col-2 text-right">
						<span><button name='${expEvent}' data-toggle="modal"
						data-target="#addCompanyDetails" class="iExpEdit btn btn-sm fa fa-edit"></button></span>
					</div>
				`);

				for(let i=0;i<6;i++) companyData[i][expEvent] = data[i];
				expEvent = undefined;
			} else {
				textInfo.append(`
					<div class="row">
					<div class="col">
						<h3>${data[0]}</h3>
						<h3>${data[1]}</h3>
						<h5><span> ${data[4]} </span> <span> ${data[5]} </span></h5>
						<h5><span> ${data[2]} </span> <span> ${data[3]} </span></h5>
					</div>
					<div class="col-2 text-right">
						<span><button name='${countOfCompanyData}' data-toggle="modal"
						data-target="#addCompanyDetails" class="iExpEdit btn btn-sm fa fa-edit"></button></span>
					</div>
					</div>
					<hr>
				  `);
				countOfCompanyData = countOfCompanyData + 1;

				for(let i=0;i<6;i++) companyData[i].push(data[i])
			}
			$("#addCompanyDetails").modal("hide");
		}
	});
})

//SCHOOL LOGIC
let schoolData = [];
$(()=>{

	let countOfSchoolData = 0;
	let schoolEvent;
	let schoolIDs = [
		['#id_school_name', '[name="studentEducation[name]"]'],
		['#id_school_degree', '[name="studentEducation[degree]"]'],
		['#id_field_of_study', '[name="studentEducation[field]"]'],
		['#id_start_school', '[name="studentEducation[from]"]'],
		['#id_end_school', '[name="studentEducation[till]"]'],
		['#id_location_of_school','[name="studentEducation[location]"]']
	]

	schoolIDs.map((item) => {
		schoolData.push(pJSON($(item[0]).val()))
	})

	//adding the data that already exists
	for (let i = 0; i < 5; i++) {
		if (checkToPut(schoolData[0][i])) {
			$("#education").append(`
				<div class="row">
					<div class="col">
						<h3>${schoolData[0][i]}</h3>
						<h5><span>${schoolData[1][i]}</span> <span>${schoolData[2][i]}</span></h5>
						<h5><span> ${schoolData[4][i]} </span> <span> ${schoolData[5][i]} </span></h5>
						<h5>${schoolData[3][i]}</h5>
				</div>
				<div class="col-2 text-right">
					<span><button name='${i}' data-toggle="modal" data-target="#addSchoolDetails" class="educationEdit btn btn-sm fa fa-edit"></button></span>
				</div>
				</div>
				<hr>
			`);
		}
	}

	$(document).on("click", ".educationEdit", (event) => {
		schoolEvent = event.target.attributes.name.value;
		for(let i=0;i<6;i++) {
			$(schoolIDs[i][1]).val(schoolData[i][schoolEvent])
		}
	});

	$('#addSchoolDetails .modal-footer > button[type="button"]').click(() => {
		if ($("#sName").val() === "") {
			$(`<span class="text-red">Must have title</span>`).insertAfter($("#sName"));
		} else {
			let data = appendFunction("studentEducation");
			let textInfo = $("#education");
			if (schoolEvent != undefined) {
				whichChild = 1 + parseInt(schoolEvent) + parseInt(schoolEvent)
				child =
					"#education > div.row:nth-child(" + whichChild + ")";
				textInfo = $(child);
				textInfo.html(`
					<div class="col">
						<h3>${data[0]}</h3>
						<h5><span>${data[1]}</span> <span>${data[2]}</span></h5>
						<h5><span> ${data[4]} </span> <span> ${data[5]} </span></h5>
						<h5>${data[3]}</h5>
					</div>
					<div class="col-2 text-right">
						<span><button name='${schoolEvent}' data-toggle="modal"
						data-target="#addSchoolDetails" class="educationEdit btn btn-sm fa fa-edit"></button></span>
					</div>
				`);

				for(let i=0;i<6;i++) schoolData[i][schoolEvent] = data[i];
				schoolEvent = undefined;
			} else {
				textInfo.append(`
					<div class="row">
					<div class="col">
						<h3>${data[0]}</h3>
						<h5><span>${data[1]}</span> <span>${data[2]}</span></h5>
						<h5><span> ${data[4]} </span> <span> ${data[5]} </span></h5>
						<h5>${data[3]}</h5>
					</div>
					<div class="col-2 text-right">
						<span><button name='${countOfSchoolData}' data-toggle="modal"
						data-target="#addSchoolDetails" class="educationEdit btn btn-sm fa fa-edit"></button></span>
					</div>
					</div>
					<hr>
			  	`);
				countOfSchoolData = countOfSchoolData + 1;
				for(let i=0;i<6;i++) schoolData[i].push(data[i])
			}
			$("#addSchoolDetails").modal("hide");
		}
	});
});

//PROJECT LOGIC
/*let projectData = [];
$(()=>{
	let countOfProjectData = 0;
	let projectEvent;
	let projectIDs = [
		['#id_project_name', '[name="userProject[name]"]'],
		['#id_project_description', '[name="userProject[description]"]'],
		['#id_project_url', '[name="userProject[url]"]'],
		['#id_start_project', '[name="userProject[from]"]'],
		['#id_end_project', '[name="userProject[till]"]'],
	]

	projectIDs.map((item) => {
		projectData.push(pJSON($(item[0]).val()))
	})

	//adding the data that already exists
	for (let i = 0; i < 5; i++) {
		if (checkToPut(projectData[0][i])) {
			$("#project").append(`
				<div class="row">
					<div class="col">
						<h1>${projectData[0][i]}</h1>
						<a href="${projectData[2][i]}" target="_blank">${projectData[2][i]}</a>
						<h5><span> ${projectData[3][i]} </span> <span> ${projectData[4][i]} </span></h5>
						<h6>${projectData[1][i]}</h6>
				</div>
				<div class="col-2 text-right">
					<button name='${i}' data-toggle="modal" data-target="#addProjectDetails" class="projectEdit btn btn-sm btn-primary fa fa-edit"></button>
				</div>
				</div>
				<hr>
			`);
		}
	}

	$(document).on("click", ".projectEdit", (event) => {
		projectEvent = event.target.attributes.name.value;
		for(let i=0;i<5;i++) {
			$(projectIDs[i][1]).val(projectData[i][projectEvent])
		}
	});

	$('#addProjectDetails .modal-footer > button[type="button"]').click(() => {
		if ($("#pName").val() === "") {
			$(`<span class="text-red">Must have title</span>`).insertAfter($("#pName"));
		} else {
			let data = appendFunction("userProject");
			let textInfo = $("#project");
			if (projectEvent != undefined) {
				whichChild = 1 + parseInt(projectEvent) + parseInt(projectEvent)
				child =
					"#project > div.row:nth-child(" + whichChild + ")";
				textInfo = $(child);
				textInfo.html(`
					<div class="col">
						<h1>${data[0]}</h1>
						<a href="${data[2]}" target="_blank">${data[2]}</a>
						<h5> <span> ${data[3]} </span> <span> ${data[4]} </span></h5>
						<h6>${data[1]}</h6>
					</div>
					<div class="col-2 text-right">
						<button name='${projectEvent}' data-toggle="modal"
						data-target="#addProjectDetails" class="projectEdit btn btn-sm btn-primary fa fa-edit"></button>
					</div>
				`);

				for(let i=0;i<5;i++) projectData[i][projectEvent] = data[i];
				projectEvent = undefined;
			} else {
				textInfo.append(`
					<div class="row">
					<div class="col">
						<h1>${data[0]}</h1>
						<a href="${data[2]}" target="_blank">${data[2]}</a>
						<h5><span> ${data[3]} </span> <span> ${data[4]} </span></h5>
						<h6>${data[1]}</h6>
					</div>
					<div class="col-2 text-right">
						<button name='${countOfProjectData}' data-toggle="modal"
						data-target="#addProjectDetails" class="projectEdit btn btn-sm btn-primary fa fa-edit"></button>
					</div>
					</div>
					<hr>
			  	`);
				countOfProjectData = countOfProjectData + 1;
				for(let i=0;i<5;i++) projectData[i].push(data[i])
			}
			$("#addProjectDetails").modal("hide");
		}
	});
})*/

//ACHIEVEMENT LOGIC
let achievementData = [];
$(()=> {
	let countOfAchievementData = 0;
	let achievementEvent;

	let achievementIDs = [
		['#id_accomplishment_title', '[name="achievement[title]"]'],
		['#id_accomplishment_description', '[name="achievement[description]"]'],
		['#id_issuer', '[name="achievement[issuer]"]'],
		['#id_issue_date', '[name="achievement[issue]"]'],
	]

	achievementIDs.map((item) => {
		achievementData.push(pJSON($(item[0]).val()))
	})

	//adding the data that already exists
	for (let i = 0; i < 5; i++) {
		if (checkToPut(achievementData[0][i])) {
			$("#achievement").append(`
				<div class="row">
					<div class="col">
					<h3>${achievementData[0][i]}</h3>
					<h5><span>${achievementData[2][i]}</span><span>${achievementData[3][i]}</span></h5>
					<h6>${achievementData[1][i]}</h6>
				</div>
				<div class="col-2 text-right">
					<span><button name='${i}' data-toggle="modal" data-target="#addAchievementDetails" class="achievementEdit btn btn-sm fa fa-edit"></button></span>
				</div>
				</div>
				<hr>
			`);
		}
	}

	$(document).on("click", ".achievementEdit", (event) => {
		achievementEvent = event.target.attributes.name.value;
		for(let i=0;i<4;i++) {
			$(achievementIDs[i][1]).val(achievementData[i][achievementEvent])
		}
	});

	$('#addAchievementDetails .modal-footer > button[type="button"]').click(() => {
		if ($("#title").val() === "") {
			$(`<span class="text-red">Must have title</span>`).insertAfter($("#title"));
		} else {
			let data = appendFunction("achievement");
			let textInfo = $("#achievement");
			if (achievementEvent != undefined) {
				whichChild = 1 + parseInt(achievementEvent) + parseInt(achievementEvent)
				child =
					"#achievement > div.row:nth-child(" + whichChild + ")";
				textInfo = $(child);
				textInfo.html(`
					<div class="col">
						<h3>${data[0]}</h3>
						<h5><span>${data[2]}</span> <span>${data[3]}</span></h5>
						<h6>${data[1]}</h6>
					</div>
					<div class="col-2 text-right">
						<span><button name='${achievementEvent}' data-toggle="modal"
						data-target="#addAchievementDetails" class="achievementEdit btn btn-sm fa fa-edit"></button></span>
					</div>
				`);

				for(let i=0;i<4;i++) achievementData[i][achievementEvent] = data[i];
				achievementEvent = undefined;
			} else {
				textInfo.append(`
					<div class="row">
					<div class="col">
						<h3>${data[0]}</h3>
						<h5><span>${data[2]}</span><span>${data[3]}</span></h5>
						<h6>${data[1]}</h6>
					</div>
					<div class="col-2 text-right">
						<span><button name='${countOfAchievementData}' data-toggle="modal"
						data-target="#addAchievementDetails" class="achievementEdit btn btn-sm fa fa-edit"></button></span>
					</div>
					</div>
					<hr>
			  	`);
				countOfAchievementData = countOfAchievementData + 1;
				for(let i=0;i<4;i++) achievementData[i].push(data[i])
			}
			$("#addAchievementDetails").modal("hide");
		}
	});
})

function saveEverything() {
	//adding company details
	//{designation:[], companyName:[], from:[], to:[],loc:[]}
	$("#id_experience_title").val(JSON.stringify(companyData[0]));
	$("#id_company_name").val(JSON.stringify(companyData[1]));
	$("#id_company_city").val(JSON.stringify(companyData[2]));
	$("#id_company_state").val(JSON.stringify(companyData[3]));
	$("#id_start_company").val(JSON.stringify(companyData[4]));
	$("#id_end_company").val(JSON.stringify(companyData[5]));

	//adding school details
	//{school:[], degree:[], field:[], from:[], to:[], loc:[]}
	$("#id_school_name").val(JSON.stringify(schoolData[0]));
	$("#id_school_degree").val(JSON.stringify(schoolData[1]));
	$("#id_field_of_study").val(JSON.stringify(schoolData[2]));
	$("#id_start_school").val(JSON.stringify(schoolData[3]));
	$("#id_end_school").val(JSON.stringify(schoolData[4]));
	$("#id_location_of_school").val(JSON.stringify(schoolData[5]));

	//adding project details
	//{name:[], description:[], url:[], from:[], to:[]}
	/*$("#id_project_name").val(JSON.stringify(projectData[0]));
	$("#id_project_description").val(JSON.stringify(projectData[1]));
	$("#id_project_url").val(JSON.stringify(projectData[2]));
	$("#id_start_project").val(JSON.stringify(projectData[3]));
	$("#id_end_project").val(JSON.stringify(projectData[4]));*/

	//{name:[], description:[], issuer:[], date:[]}
	$("#id_accomplishment_title").val(JSON.stringify(achievementData[0]));
	$("#id_accomplishment_description").val(JSON.stringify(achievementData[1]));
	$("#id_issuer").val(JSON.stringify(achievementData[2]));
	$("#id_issue_date").val(JSON.stringify(achievementData[3]));

	setTimeout(()=>{
		$("#finalSaveButton").click()
		}, 800)
}

$("#mainSave").on("click", () => {
	saveEverything()
});


