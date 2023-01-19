import React, { useState, useEffect } from 'react';

class Card extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return(
            <div>
                <div>
                    <p> First name: {this.props.items.firstname}</p>
                </div>
                <div>
                    <p> Last name: {this.props.items.lastname} </p>
                </div>
                <div>
                    <p> Job: {this.props.items.job_title} </p>
                </div>
                <div>
                    <p> Email: {this.props.items.email}</p>
                </div>
                <div>
                    <p> Description: {this.props.items.description} </p>
                </div>
            </div>
        )
    }
}

export default Card;