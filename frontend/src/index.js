import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
//Redux Store/Provider
import store from './redux/store';
import { Provider } from 'react-redux';
// React Bootstrap 
import './bootstrap.min.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}  >
    <App />
  </Provider>
);

