import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

export async function sendPerception(payload) {
  const response = await axios.post(
    `${API_BASE}/perception/teach`,
    payload
  );
  return response.data;
}
