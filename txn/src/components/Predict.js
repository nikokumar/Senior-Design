import React from "react";
import Button from '@material-ui/core/Button';
import '../index.css';
import {Link } from "react-router-dom";

    function Predict() {

        return (
            <Link to="/predictionResults" style={{textDecoration: 'none'}}>
            <Button class = "btn" style={{color: '#FFFFFF', fontSize: 20, fontWeight: 'bold', textDecoration: 'none', textTransform: "none"}}> Predict </Button>
            </Link>
        );

    }

    export default Predict;