import axios from 'axios';

const API_URL = 'http://localhost:5000/api/users';

const getUsers = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('There was an error fetching the users!', error);
    throw error;
  }
};

export default {
  getUsers
};