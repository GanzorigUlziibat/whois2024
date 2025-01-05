export async function sendRequest(_url, _method, _body) {
  try {
    const response = await fetch(_url, {
      method: _method,
      body: _body,
    });
    const data = await response.json();
    return data;
  } catch (e) {
    return e.message;
  }
}

