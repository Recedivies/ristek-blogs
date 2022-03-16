import React, { useState } from "react";
import axios from "../services/apiClient";
import { toast } from "react-toastify";

const Test = () => {
  const [textInput, setTextInput] = useState("");
  const [output, setOutput] = useState("");

  const handleSubmit = () => {
    axios
      .get(`/api/blogs/test?text=${textInput}`)
      .then((res) => {
        toast.success("successfully bla bla bla");
        setOutput(res.data.text);
      })
      .catch((err) => {
        toast.error(
          `${JSON.stringify(err.response.data.detail)} (${err.response.status})`
        );
        console.log(err.message);
      });
  };

  return (
    <div>
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

export default Test;
