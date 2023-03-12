import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

import {PersistGate} from 'redux-persist/integration/react'; // null - compopnent при загрузке
import { Provider } from 'react-redux';

import store, {persistor} from './store/store';


const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render( 
    <Provider store={store}>
        <PersistGate loading={null} persistor={persistor}></PersistGate> 
        <React.StrictMode>
            <App />
        </React.StrictMode>
    </Provider>
);


