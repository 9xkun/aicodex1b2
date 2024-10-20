import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Navigation from './Navigation';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import UserAddPage from './pages/UserAddPage';
import TaskAddPage from './pages/TaskAddPage';


function App() {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <Routes>
          <Route exact path="/" element={<HomePage />} />
          <Route path="/user-add" element={<UserAddPage />} />
          <Route path="/task-add" element={<TaskAddPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
