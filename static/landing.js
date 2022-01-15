const $landingSigningButton = document.querySelector('#landing-btn-login')
const $landingModal = document.querySelector('#landing-modal')

$landingSigningButton.addEventListener('click', () => {
    $landingModal.style.removeProperty('display')
})

$landingModal.addEventListener('click', (event) => {
    if (event.target.classList.contains("modal-outer")){
        $landingModal.style.display='none'
    }
})