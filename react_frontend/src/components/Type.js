import PropTypes from 'prop-types'

export const Type = ({type, width, onClick}) => {
    return (
        <div className='block' style={{width: `${width}%`}} onClick={() => onClick(type, 1)}>
            {type}
        </div>
    )
}
Type.propTypes = {
    type: PropTypes.string,
    onClick: PropTypes.func,
}