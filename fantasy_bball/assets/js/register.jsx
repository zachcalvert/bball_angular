var React = require('react')


var handleGroceryClick = function(i, items) {
  console.log('You clicked: ' + items[i]);
}

function GroceryList(props) {  
  return (
    <div>
      {props.items.map(function(item, i) {
        return (
          <div onClick={handleGroceryClick.bind(this, i, props.items)} key={i}>{item}</div>
        );
      })}
    </div>
  );
}

ReactDOM.render(
  <GroceryList items={['Apple', 'Banana', 'Cranberry']} />, mountNode
);