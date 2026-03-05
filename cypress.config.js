const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    //baseUrl: 'http://localhost:8000',
    specPattern: 'cypress/e2e/**/*.cy.js', 
    supportFile: 'cypress/support/e2e.js',
    viewportWidth: 1280,
    viewportHeight: 720,
    video: true,
  },
  env: {
    apiUrl: 'http://localhost:8000',
  },
});