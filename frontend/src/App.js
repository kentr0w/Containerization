import './App.css';
import React, { useState, useEffect } from 'react';

function App() {

	return (
		<div className="App">
		<h1>List of business cards:</h1>
		<hr/>

		{/* <div className="card-container">
		{data.map((item, index) => (
		<div className="card" key={index}>
		<h2>{item.name}</h2>
		<p>{item.company}</p>
		<p>{item.jobtitle}</p>
		<p>{item.email}</p>
		<p>{item.phone}</p>
		</div>
		))}
		</div> */}

		<h1>Add Your Own Business Card To The List!</h1>
		<form action="http://localhost:5000/users/" method="POST">
		<label for="firstname">Firstname:</label><br/>
		<input name="firstname" type="text"/><br/>
		<label for="company">Company:</label><br/>
		<input name="lastname" type="text"/><br/>
		<label for="jobtitle">Job title:</label><br/>
		<input name="job_title" type="text"/><br/>
		<label for="email">Email:</label><br/>
		<input name="email" type="text"/><br/>
		<label for="description">Description:</label><br/>
		<input name="description" type="text"/><br/>
		<input type="submit" value="register"/>
		</form>
		</div>
		);
	}

export default App;
