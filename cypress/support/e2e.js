// cypress/support/e2e.ts
// Este archivo se carga automáticamente antes de cada spec (.cy.ts)

import './commands'; // Importa los comandos personalizados definidos en commands.ts
// Ejemplo: comando custom simple (opcional por ahora)
beforeEach(() => {
  // cy.log('Support file cargado - Cypress inicializado');
  // cy.viewport(1280, 720);   // ejemplo útil si querés viewport fijo
});

