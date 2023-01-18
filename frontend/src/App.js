import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
	<h1>List of registered people</h1>
      	<hr/>
      	<h1>Register Yourself</h1>
      	<label for="firstname">Firstname:</label><br/>
      	<input type="text"/><br/>
     	<label for="lastname">Lastname:</label><br/>
      	<input type="text"/><br/>
      	<label for="email">Email:</label><br/>
      	<input type="text"/><br/>
      	<input type="submit" value="register"/>
    </div>
  );
}

export default App;
