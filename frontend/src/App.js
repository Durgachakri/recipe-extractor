import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [recipe, setRecipe] = useState(null);
  const [history, setHistory] = useState([]);

  const extractRecipe = async () => {
    const res = await axios.post(
      `http://127.0.0.1:8000/extract?url=${url}`
    );
    setRecipe(res.data);
    loadHistory();
  };

  const loadHistory = async () => {
    const res = await axios.get("http://127.0.0.1:8000/recipes");
    setHistory(res.data);
  };

  useEffect(() => {
    loadHistory();
  }, []);

  return (
    <div className="container">
      <h1>Recipe Extractor</h1>

      {/* TAB 1 */}
      <div className="card">
        <input
          placeholder="Enter Recipe URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={extractRecipe}>Extract</button>

        {recipe && (
          <div>
            <h2>{recipe.title}</h2>

            <h3>Ingredients</h3>
            <ul>
              {recipe.ingredients.map((i, idx) => (
                <li key={idx}>{i.item}</li>
              ))}
            </ul>

            <h3>Instructions</h3>
            <ul>
              {recipe.instructions.map((s, idx) => (
                <li key={idx}>{s}</li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {/* TAB 2 */}
      <div className="card">
        <h2>History</h2>
        {history.map((r) => (
          <div key={r.id}>
            <h4>{r.title}</h4>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;