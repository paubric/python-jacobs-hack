import React from 'react'

const Entities = ({ entities }) => {
  return (
    <div>
      {entities.map((entity) => (
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{entity.name}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{entity.type}</h6>
            <p class="card-text">{entity.average_sentiment}</p>
          </div>
        </div>
      ))}
    </div>
  )
};

export default Entities