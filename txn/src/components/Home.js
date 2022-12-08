import React from 'react';
import ButtonAppBar from './Navbar';
import Predict from "./Predict";
import '../index.css';
import RangeField from "./dateRangeField"

require('typeface-dm-sans');

const Home = () =>  {
    return (
        <html>
            <ButtonAppBar/>
            <body style={{backgroundColor: '#CC5500'}}>
        

        <h1 className = "heavyspacer" align = "center" style={{ color: 'white', fontSize: 70, fontWeight: 'bold' }}>$TXN Trading Predictor</h1>
    
  
        <p className = "spacer" align = "center" style={{ color: 'white', fontSize: 24}}>
        Please select a prediction range:
        </p>
        <div className = "spacer" align = "center">
        <RangeField/>
            <Predict/>
            </div>
            
        

        
        
        </body>
        </html>
    );
    }
    export default Home;