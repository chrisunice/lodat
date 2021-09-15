import React from 'react';
import { makeStyles } from "@material-ui/core/styles";
import ArrowForwardIcon from '@material-ui/icons/ArrowForward';
import ArrowBackIcon from '@material-ui/icons/ArrowBack';



const useStyles = makeStyles({
    controlContainer: {
        display: 'flex',
        justifyContent: 'center',
        border: '2px solid green' // note debugging only
    },
    arrowContainer: {
        display: 'flex',
        justifyContent: 'space-evenly',
        width: '20vw',
        border: '2px solid yellow'
    },
    arrow: {
        fontSize: 'xxx-large',
        color: "white"
    }
});

const ControlContainer = () => {
    const classes = useStyles();
    return (
        <div className={classes.controlContainer}>
            <div className={classes.arrowContainer}>
                <ArrowBackIcon className={classes.arrow} />
                <ArrowForwardIcon className={classes.arrow} />
            </div>
        </div>
    );
}

export default ControlContainer;
