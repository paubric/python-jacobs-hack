import React from 'react'

const Entities = ({ colorizer, entities }) => {
  return (
    <div>
      {entities.map((entity) => (
        <>
        <div class="card" style={{backgroundColor: colorizer(entity.average_sentiment)}} >
          <div class="card-body">
            <h5 class="card-title">{entity.name}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{entity.type}</h6>
            <p class="card-text">{1 - (0.5 + entity.average_sentiment/2)}</p>
          </div>
        </div>
        <br/>
        </>
      ))}
    </div>
  )
};

export default Entities