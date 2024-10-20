import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { BrowserRouter as Router } from 'react-router-dom';
import axios from 'axios';
import HomePage from './HomePage';

// Mock axios
// UI Tests
jest.mock('axios');

describe('HomePage', () => {
  test('renders loading spinner initially', () => {
    axios.get.mockResolvedValue({ data: [] });
    render(
      <Router>
        <HomePage />
      </Router>
    );
    expect(screen.getByRole('status')).toBeInTheDocument();
  });

  test('renders user list after fetching data', async () => {
    const users = [
      { id: 1, firstname: 'John', lastname: 'Doe', email: 'john@example.com', phone: '123-456-7890', age: 30 },
      { id: 2, firstname: 'Jane', lastname: 'Doe', email: 'jane@example.com', phone: '098-765-4321', age: 25 },
    ];
    axios.get.mockResolvedValue({ data: users });

    render(
      <Router>
        <HomePage />
      </Router>
    );

    await waitFor(() => expect(screen.getByText('User List')).toBeInTheDocument());

    users.forEach(user => {
      expect(screen.getByText(user.firstname + ' ' + user.lastname)).toBeInTheDocument();
      expect(screen.getByText(user.email)).toBeInTheDocument();
      expect(screen.getByText(user.phone)).toBeInTheDocument();
      expect(screen.getByText(user.age.toString())).toBeInTheDocument();
    });
  });

  test('renders error message on fetch failure', async () => {
    axios.get.mockRejectedValue(new Error('There was an error fetching the users!'));

    render(
      <Router>
        <HomePage />
      </Router>
    );

    await waitFor(() => expect(screen.queryByRole('status')).not.toBeInTheDocument());
    expect(screen.queryByText('User List')).not.toBeInTheDocument();
  });

  test('renders Add User button', () => {
    axios.get.mockResolvedValue({ data: [] });
    render(
      <Router>
        <HomePage />
      </Router>
    );
    expect(screen.getByText('Add User')).toBeInTheDocument();
  });
});