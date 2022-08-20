"use strict";
var KTUsersAddUser=function() {
	const t=document.getElementById("kt_modal_add_user"),
	e=t.querySelector("#kt_modal_add_user_form"),
	n=new bootstrap.Modal(t);
	return { 
		init: 
			function() {(() => { 
				var o=FormValidation.formValidation(e, { 
					fields : {
						user_name : {
							validators: {
								notEmpty: {message:"Full name is required"}
							}
						},
						user_email: {
							validators: {
								notEmpty: {message:"Valid email address is required"}
							}
						}
					},
					plugins: {
						trigger:new FormValidation.plugins.Trigger,
						bootstrap:new FormValidation.plugins.Bootstrap5({rowSelector:".fv-row",eleInvalidClass:"",eleValidClass:""})
					}
				});
				const i=t.querySelector('[data-kt-users-modal-action="submit"]');
				i.addEventListener(
					"click", 
					(t => {
						t.preventDefault(),
						o&&o.validate().then(
							(function(t) {
								if (t == "Valid") {
									i.setAttribute("data-kt-indicator","on"),
									i.disabled=!0,
									i.removeAttribute("data-kt-indicator"),
									i.disabled=!1,
									Swal.fire({text:"User has been successfully created",icon:"success",buttonsStyling:!1,confirmButtonText:"Ok, got it!",customClass:{confirmButton:"btn btn-primary"}})
										.then((function(t){t.isConfirmed&&n.hide()}))
								}
							})
						)
					})
				)
			}) ()
		}
	}
}();

KTUtil.onDOMContentLoaded((function(){KTUsersAddUser.init()}));