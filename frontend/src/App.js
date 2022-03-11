import { useState } from "react";
import axios from "./utils/apiClient";

const App = () => {
  const [textInput, setTextInput] = useState("");
  const [output, setOutput] = useState("");

  const handleSubmit = () => {
    axios
      .get(`/api/blogs/test?text=${textInput}`)
      .then((res) => {
        setOutput(res.data.text);
      })
      .catch((err) => console.log(err));
  };
  return (
    <div className="App">
      <h1>Hello World</h1>

      <div>
        <p>Test connection with API:</p>
        <label htmlFor="char-input">Make this text uppercase: </label>
        <input
          id="char-input"
          type="text"
          value={textInput}
          onChange={(e) => setTextInput(e.target.value)}
        />
        <button onClick={handleSubmit}>Submit</button>
        <h3>{output}</h3>
      </div>
    </div>
  );
};

export default App;
