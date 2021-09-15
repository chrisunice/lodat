import { makeStyles, ThemeProvider } from "@material-ui/core/styles";

import MenuBar from './components/MenuBar';
import ImageContainer from './components/ImageContainer';
import ControlContainer from './components/ControlContainer';


const useStyles = makeStyles((theme) => ({
    application: {
        display: 'flex',
        flexDirection: 'column',
        width: '100vw',
        height: '100vh',
        backgroundColor: '#808080',
    }
}));

const App = () => {
    const classes = useStyles()

    return (
        <div className={classes.application}>
            <MenuBar />
            <ImageContainer source='https://nationalinterest.org/sites/default/files/styles/desktop__1260_/public/main_images/1341px-B-2_first_flight_071201-F-9999J-034.jpg' />
            <ControlContainer />
        </div>
    )
}

export default App;
