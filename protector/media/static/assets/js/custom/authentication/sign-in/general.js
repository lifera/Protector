"use strict";
var KTSigninGeneral = function() {
	var t,e,i;
	return {
		init:function() {
			t=document.querySelector("#kt_sign_in_form"),
			e=document.querySelector("#kt_sign_in_submit"),
			i=FormValidation.formValidation(t, {
				fields: {
					email: {
						validators: {
							notEmpty: {
								message: "Email address is required"
							},
							emailAddress: {
								message: "The value is not a valid email address"
							}
						}
					},
					password: {
						validators: {
							notEmpty: {
								message: "The password is required"
							}
						}
					}
				},
			
				plugins: {
					trigger: new FormValidation.plugins.Trigger,
					bootstrap: new FormValidation.plugins.Bootstrap5({rowSelector:".fv-row"})
				}
			}),
			e.addEventListener("click",(function(n) {
				n.preventDefault(),
				i.validate().then((function(i) {
					if (i == "Valid") {
						e.setAttribute("data-kt-indicator","on"),
						e.disabled=!0,
						e.removeAttribute("data-kt-indicator"),
						e.disabled=!1,
						location.href=t.getAttribute("data-kt-redirect-url")
					}
				}))
			}))
		}
	}
}();
							
KTUtil.onDOMContentLoaded((function(){KTSigninGeneral.init()}));