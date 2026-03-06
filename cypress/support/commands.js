
Cypress.Commands.add('logStep', (message) => {
  cy.log(`[STEP] ${message}`);
  // Optional: cy.screenshot() or other logging actions
});