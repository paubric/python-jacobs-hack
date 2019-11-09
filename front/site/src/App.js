import React, { Component } from 'react';
import Entities from './components/entities';

class App extends Component {
  constructor (props){
    super(props);
  
    this.state = {
      entities: [],
      query: ""
    }    
  }

  handleChange = event => {
    const value = event.target.value;
    this.setState({
      query: value
    });
  };

  updateEntities = event => {
    console.log(this.state);

    fetch('https://us-central1-playground-256616.cloudfunctions.net/jacobs/api?query='+this.state.query)
    .then(res => res.json())
    .then((data) => {

      var keys = Object.keys(data);
      keys.forEach(function(key){
          data[key]['name'] = key;
          console.log(data);
      });

      var values = Object.keys(data).map(function(key){
        return data[key];
      });

      this.setState({ entities: values })
      console.log(data)
    })
    .catch(console.log)
  }

  render() {
    return (
      <>
      <center>
      <div class="jumbotron">
      <h1 class="display-4">Standpoint</h1>
      <p class="lead">Democratizing political intelligence</p>
      <p>Enter the text you want to analyze below.</p>
      <p class="lead">
      <input
            type="text"
            value={this.state.value}
            onChange={this.handleChange}
         /> <button onClick={this.updateEntities} class="btn btn-primary">Go</button>      
      </p>
      </div>
      </center>
      
      <Entities entities={this.state.entities} />
      </>
    )
  }
  
}

export default App