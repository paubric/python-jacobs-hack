import React, { Component } from 'react';
import Entities from './components/entities';

class App extends Component {
  constructor (props){
    super(props);
  
    this.state = {
      entities: [],
      query: "",
      objectivity: '',
      popularity: '',
      optimism: ''
    }    
  }

  handleChange = event => {
    const value = event.target.value;
    this.setState({
      query: value
    });
  };

  getColorForPercentage = function(value){
    //value from 0 to 1
    var hue=((1-value)*120).toString(10);
    return ["hsl(",hue,",100%,50%)"].join("");
}

  updateEntities = event => {
    console.log(this.state);

    fetch('https://us-central1-playground-256616.cloudfunctions.net/jacobs/api?query='+this.state.query
    )
    .then(res => res.json())
    .then((data) => {

      console.log(data);

      var entities = data['entities']
      var keys = Object.keys(entities);
      keys.forEach(function(key){
        entities[key]['name'] = key;
          console.log(entities);
      });

      var values = Object.keys(entities).map(function(key){
        return entities[key];
      });

      values = values.filter(function(object) {
        return object.average_magnitude > 0.9;
      });

      values = values.sort((a,b) => a.average_sentiment - b.average_sentiment );

      this.setState({ entities: values,
        objectivity: data['objectivity'],
        popularity: data['popularity'],
        optimism: data['optimism'],
      })
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
      <p>Enter the name of the entity you want to analyze below.</p>
      <p class="lead">
      <input
            type="text"
            value={this.state.value}
            onChange={this.handleChange}
         /> <button onClick={this.updateEntities} class="btn btn-primary">Go</button>      
      </p>
      </div>
      </center>
      <div style={{margin: "0 auto", width: "855px"}}>
      <div class="row">
        <div class="col-sm-4">
        <div class="card">
            <div class="card-header">
              Objectivity
            </div>
            <div class="card-body">
              <h5 class="card-title">{this.state.objectivity}</h5>
            </div>
          </div>
        </div>
        <div class="col-sm-4">
        <div class="card">
            <div class="card-header">
              Popularity
            </div>
            <div class="card-body">
              <h5 class="card-title">{this.state.popularity}</h5>
            </div>
          </div>
        </div>
        <div class="col-sm-4">
        <div class="card">
            <div class="card-header">
              Optimism
            </div>
            <div class="card-body">
              <h5 class="card-title">{this.state.optimism}</h5>
            </div>
          </div>
          <br/>
        </div>
      <br/>
      </div>
      <br/>
        <Entities colorizer={this.getColorForPercentage} entities={this.state.entities} />
      </div>
      </>
    )
  }
  
}

export default App