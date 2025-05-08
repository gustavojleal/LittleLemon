

const modals = {
  config: {
    login: {
      id: 'loginModal',
      formId: 'loginForm',
      openTrigger: '[data-modal-target="#loginModal"]'
    },
    signup: {
      id: 'signupModal',
      formId: 'signupForm',
      openTrigger: '[data-modal-target="#signupModal"]'
    }
  },


  init: function () {
    // Event Listeners open modal
    document.querySelectorAll(this.config.signup.openTrigger).forEach(btn => {
      btn.addEventListener('click', () => this.showModal('signup'));
    });

    document.querySelectorAll(this.config.login.openTrigger).forEach(btn => {
      btn.addEventListener('click', () => this.showModal('login'));
    });


    // Global Event Listeners 
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') this.closeActiveModal();
    });

    this.checkErrorsOnLoad();
  },


  showModal: function (type) {
    const modalId = this.config[type].id;
    const modal = document.getElementById(modalId);

    if (modal) {
      const openModals = document.querySelectorAll('.modal-overlay[style*="display: flex"]');
      openModals.forEach(existingModal => {
        if (existingModal !== modalId) {
          existingModal.style.display = 'none';
        }
      })
      modal.style.display = 'flex';
      const firstInput = modal.querySelector('input');
      if (firstInput) firstInput.focus();
    }
  },

  closeActiveModal: function () {
    const activeModal = document.querySelector('.modal-overlay[style*="display: flex"]');
    if (activeModal) {
      activeModal.style.display = 'none';
      this.resetForm(activeModal.querySelector('form'));
    }
  },

  closeAllModals: function () {
    document.querySelectorAll('.modal-overlay').forEach(modal => {
      modal.style.display = 'none';
      this.resetForm(modal.querySelector('form'));
    });
  },

  resetForm: function (form) {
    if (form) {
      form.reset();
      form.querySelectorAll('.error-message').forEach(el => el.textContent = '');
    }
  },

  checkErrorsOnLoad: function () {  //for each modal
    // Login
    if (document.getElementById('loginForm')?.querySelector('.error-message')) {
      this.showModal('login');
    }

    // Signup
    if (document.getElementById('signupForm')?.querySelector('.error-message')) {
      this.showModal('signup');
    }
  }
};

// Start DOM is ready
document.addEventListener('DOMContentLoaded', () => modals.init());

// Click outside modal
document.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-overlay')) {
    modals.closeActiveModal();
  }
});



