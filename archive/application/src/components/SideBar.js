import React, {useState} from 'react';
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    sidebarContainer: {
        display: "flex",
        flexDirection: "column",
        alignItems: 'center',
        width: 300,
        padding: 10,
        height: "100vw",
        // left: "-100%",
        border: '1px solid black',
        backgroundColor: '#29b6f6ff',
        boxShadow: "5px 0px 10px -2px darkgray"
    },
    dropdown: {
        height: 50,
        fontSize: 'large',
        width: '100%',
        textAlign: 'left',
        margin: 10
    }
}));

const SideBar = () => {
    const classes = useStyles()
    const [sidebar, setSidebar] = useState(false);
    const showSidebar = () => {
    setSidebar(!sidebar);
    }
    return (
        <div className={classes.sidebarContainer}>
            <h2>Search Options</h2>
            <select name="database" id="database-select" className={classes.dropdown}>
                <option value="">Select a database</option>
                <option value="">db_to_be_provided_by_server.sqlite</option>
            </select>
            <select name="platform" id="platform-select" className={classes.dropdown}>
                <option value="">Select a platform</option>
                // todo needs to be populated by whats available in the selected database
            </select>
            <select name="tail" id="tail-select" className={classes.dropdown}>
                <option value="">Select a tail</option>
                // todo needs to be populated by whats available in the selected database
            </select>
            <select name="tail" id="tail-select" className={classes.dropdown}>
                <option value="">Select a UMI</option>
                // todo needs to be populated by whats available in the selected database
            </select>
        </div>
    );
};

export default SideBar;