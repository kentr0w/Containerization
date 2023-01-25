import React, { useState, useEffect } from 'react';
import Card from './Card';

function Cards() {
    const [items, setItems] = useState([]);

    useEffect(() => {
      fetch('http://flaskapi:5001/users/')
        .then(res => res.json())
        .then(data => setItems(data.keys));
    }, []);

    return (
      <div>
        {items.map((it, index) =>
            <div>
                <Card key = {index} items = {it} />
                <hr/>
            </div>
        ).reverse()}
      </div>
    );
}

export default Cards;
