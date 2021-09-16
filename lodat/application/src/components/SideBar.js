import React from 'react';
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    sidebarContainer: {
        width: '25vw',
        height: '100vh',
        position: 'fixed',
        // left: "-100%",
        backgroundColor: '#29b6f6ff',
        boxShadow: "0px 1px 10px 5px lightgray"
    }
}));

const SideBar = () => {
    const classes = useStyles()
    return (
        <div className={classes.sidebarContainer}>
            <select name="database" id="database-select">
                <option value="">Select a database</option>
            </select>
        </div>
    );
};

export default SideBar;