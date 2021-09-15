import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles({
  imageContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    height: 'auto',
    padding: 50,
    border: '2px solid red' // note debugging only
  },
  image: {}
});

const ImageContainer = (props) => {
  const classes = useStyles();
  return (
      <div className={classes.imageContainer}>
        <img src={props.source} alt=""/>
      </div>
  );
}

ImageContainer.defaultProps = {
  source: ''
};

Image.propTypes = {
  title: PropTypes.string
};

export default ImageContainer;
