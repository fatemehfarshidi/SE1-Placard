import React, {useState} from 'react';
import Login from './LoginSignup/Login';
import Register from './LoginSignup/Register';

function App() {
  //to show which page should be displayed at each moment 
  const [currentForm, setCurrentForm] = useState('login');

  //switch from pages through buttons
  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  return (
    <div className="App">
      
      { // either shows login or Register page 
        currentForm === "login" ? <Login onFormSwitch={toggleForm} /> : <Register onFormSwitch={toggleForm} />
      }
      
    </div>
  );
}

export default App;
