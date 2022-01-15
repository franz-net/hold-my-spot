// Variables and Constants
const $landingSigningButton = document.querySelector('#landing-btn-login')
const $landingModal = document.querySelector('#landing-modal')
const $loginSignupTabs = document.querySelectorAll('.login-tablink')
const $loginSignupContent = document.querySelectorAll('.login-tabcontent')
const $defaultLoginTab = document.querySelector('.default')

// Functions

function loginTabs(evt, action) {
    
    for (let tabcontent of $loginSignupContent) {
        /* tabcontent.style.display="none" */
        tabcontent.classList.add("tabcontent-hide")
    }

    for (let btn of $loginSignupTabs) {
        btn.className = btn.className.replace(" active", "")
    }

    evt.currentTarget.className += " active"
    /* document.getElementById(action).style.display="block" */
    document.getElementById(action).classList.add('tabcontent-show')
    document.getElementById(action).classList.remove('tabcontent-hide')

}


// Dom interactions
$landingSigningButton.addEventListener('click', () => {
    $landingModal.style.removeProperty('display')
})

$landingModal.addEventListener('click', (event) => {
    if (event.target.classList.contains("modal-outer")){
        $landingModal.style.display='none'
    }
})

for (let tab of $loginSignupTabs) {
    tab.addEventListener('click', (event) => {
        if (event.target.innerText === "Login") {
            loginTabs(event, "login-details")
        } else {
            loginTabs(event, "signup-details")
        }
    })
}

$defaultLoginTab.click()