import React from 'react';
import { Link } from 'react-router-dom';
import { FaSpinner } from 'react-icons/fa';
import useUsers from '../hooks/useUserLists';

function HomePage() {
  const { users, loading, error } = useUsers();

  return (
    <div className="container mt-5">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <h1>User List</h1>
        <Link to="/user-add" className="btn btn-primary">Add User</Link>
      </div>
      {loading ? (
        <div className="text-center">
          <FaSpinner className="fa-spin" size={50} />
        </div>
      ) : error ? (
        <div className="alert alert-danger">There was an error fetching the users!</div>
      ) : (
        <table className="table table-striped table-bordered">
          <thead className="thead-dark">
            <tr>
              <th>ID</th>
              <th>Full Name</th>
              <th>Email</th>
              <th>Phone</th>
              <th>Age</th>
            </tr>
          </thead>
          <tbody>
            {users.map(user => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.firstname + ' ' + user.lastname }</td>
                <td>{user.email}</td>
                <td>{user.phone}</td>
                <td>{user.age}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default HomePage;
