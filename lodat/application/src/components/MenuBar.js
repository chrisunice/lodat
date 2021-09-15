import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

const useStyles = makeStyles({
  menuContainer: {
    display: 'flex',
    alignItems: 'top',
    border: '2px solid blue' // note debugging only
  },
  menuButton: {},
  menuTitle: {}
});

const MenuBar = () => {
  const classes = useStyles();

  return (
    <div className={classes.menuContainer}>
      <AppBar position="static">
        <Toolbar>
          <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" className={classes.menuTitle}></Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default MenuBar;