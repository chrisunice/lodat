import React from 'react';
import { makeStyles } from "@material-ui/core/styles";
import { FaArrowAltCircleLeft, FaArrowAltCircleRight } from "react-icons/fa";


const useStyles = makeStyles({
    controlContainer: {
        display: 'flex',
        justifyContent: 'center',
    },
    arrowContainer: {
        display: 'flex',
        justifyContent: 'space-evenly',
        width: 200,
        borderRadius: 10,
        boxShadow: "-1px -1px 10px 8px darkgrey",
        backgroundColor: "white",
        padding: "10px 25px 10px 25px",
    },
    arrow: {
        fontSize: 'xxx-large',
        color: "black"
    }
});

const ControlBar = () => {
    const classes = useStyles();
    return (
        <div className={classes.controlContainer}>
            <div className={classes.arrowContainer}>
                <FaArrowAltCircleLeft className={classes.arrow} />
                <FaArrowAltCircleRight className={classes.arrow} />
            </div>
        </div>
    );
}

export default ControlBar;
