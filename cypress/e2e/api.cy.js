describe('API Testing con Cypress - Todo API', () => {

  const apiUrl = Cypress.env('apiUrl') || 'http://localhost:8000';

  it('GET /todos/ - debería retornar lista de todos', () => {
    cy.request(`${apiUrl}/todos/`).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.be.an('array');
      expect(response.body.length).to.be.greaterThan(0);
      expect(response.body[0]).to.have.property('title');
    });
  });

  it('GET /todos/1 - debería retornar un todo específico', () => {
    cy.request(`${apiUrl}/todos/1`).its('body').should('include', {
      id: 1,
      title: 'Comprar leche',
    });
  });

  it('POST /todos/ - debería crear un nuevo todo', () => {
    const newTodo = {
      id: 100,
      title: 'Cypress test todo',
      completed: false,
    };

    cy.request({
      method: 'POST',
      url: `${apiUrl}/todos/`,
      body: newTodo,
      failOnStatusCode: false,
    }).then((response) => {
      expect(response.status).to.eq(201);
      expect(response.body.title).to.eq('Cypress test todo');
    });
  });

  it('GET todo inexistente - debería fallar con 404', () => {
    cy.request({
      url: `${apiUrl}/todos/9999`,
      failOnStatusCode: false,
    }).its('status').should('eq', 404);
  });
});