
Cypress.Commands.add('logStep', (message) => {
  cy.log(`[STEP] ${message}`);
  // Opcional: cy.screenshot() u otras acciones
});