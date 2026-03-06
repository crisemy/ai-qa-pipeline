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

  it('GET /todos/1 - Returns a specific todo', () => {
    cy.request(`${apiUrl}/todos/1`).its('body').should('include', {
      id: 1,
      title: 'Buy milk',
    });
  });

  it('POST /todos/ - Returns a specific todo', () => {
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

  it('GET non-existent todo - should fail with 404', () => {
    cy.request({
      url: `${apiUrl}/todos/9999`,
      failOnStatusCode: false,
    }).its('status').should('eq', 404);
  });
});