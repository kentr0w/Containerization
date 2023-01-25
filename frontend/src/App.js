import './App.css';
import React, { useState, useEffect } from 'react';
import Card from './Cards';

class App extends React.Component {

	render() {
		return (
			<div className="App">			
				<iframe name="hiddenFrame" class="hide"></iframe>
				<h1>Add Your Own Business Card To The List!</h1>
				<form name="form" action="http://flaskapi:5001/users/" method="POST" target="hiddenFrame" onsubmit="setTimeout(function () { window.location.reload(); }, 500)">
					<label for="firstname">Full Name:</label><br/>
					<input name="firstname" type="text"/><br/>
					<label for="company">Company:</label><br/>
					<input name="lastname" type="text"/><br/>
					<label for="jobtitle">Job Title:</label><br/>
					<input name="job_title" type="text"/><br/>
					<label for="email">Email:</label><br/>
					<input name="email" type="text"/><br/>
					<label for="description">Description:</label><br/>
					<input name="description" type="text"/><br/>
					<input type="submit" value="register"/>
				</form>
				<hr/>
				<h1>List Of Previous Business Cards:</h1>
				<Card></Card>
			</div>
			);
		}
	}

export default App;
