import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState(null);
  const onClick = ()=>{
    axios.get('https://newsapi.org/v2/top-headlines?country=kr&apiKey=69e6bc821b9741e4aee5489a4ba2984b')
    .then(response => {
      setData(response.data);
    });
  };
  return (
    <div className="App">
      <div>
        <button onClick={onClick}>불러오기</button>
      </div>
      {data && <textarea rows={7} value={JSON.stringify(data, null, 2)} readOnly={true} />}
    </div>
  );
}

export default App;
