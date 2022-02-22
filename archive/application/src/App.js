import { useState } from 'react';
import { makeStyles } from "@material-ui/core/styles";

import SideBar from "./components/SideBar";
import MenuBar from './components/MenuBar';
import Image from './components/Image';
import ControlBar from './components/ControlBar';


const useStyles = makeStyles((theme) => ({
    app: {
        display: 'flex',
        flexDirection: 'column',
        width: '100vw',
        height: '100vh',
        backgroundColor: 'gray',
    },
    body: {
        display: 'flex',
        flexDirection: 'row',
    },
    display: {
        display: 'flex',
        flexDirection: "column",
        alignItems: 'center',
        width: '100%'
    }
}));

const App = () => {
    const classes = useStyles()

    const [state, setState] = useState({
        sidebar: false
    })
    // note this is where I left off
    const showSidebar = () => {
        setState({sidebar: !sidebar})
    }

    return (
        <div className={classes.app}>
            <MenuBar />
            <div className={classes.body}>
                <SideBar />
                <div className={classes.display}>
                    <Image source='https://nationalinterest.org/sites/default/files/styles/desktop__1260_/public/main_images/1341px-B-2_first_flight_071201-F-9999J-034.jpg' />
                    <ControlBar />
                </div>
            </div>
        </div>
    )
}

export default App;
