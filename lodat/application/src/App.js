import { makeStyles, ThemeProvider } from "@material-ui/core/styles";

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
    appContents: {
        flexDirection: 'column',
        width: '100vw'
    },
}));

const App = () => {
    const classes = useStyles()

    return (
        <div className={classes.app}>
            <SideBar />
            <MenuBar />
            <Image source='https://nationalinterest.org/sites/default/files/styles/desktop__1260_/public/main_images/1341px-B-2_first_flight_071201-F-9999J-034.jpg' />
            <ControlBar />
        </div>
    )
}

export default App;
