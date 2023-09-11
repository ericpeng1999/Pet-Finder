import PropTypes from 'prop-types'


export const SmallProfile = ({width, onClick, ele}) => {    
    return (
        <div className="block" style={{width: `${width}%`, height:'310px'}} onClick={() => onClick(ele['id'])}>
            <img src={ele['imgURL']} alt=''/>
            <h4>{ele['name']}</h4>
            <h6>{ele['description']}</h6>
        </div>
    )
}
SmallProfile.propTypes = {
    width: PropTypes.number,
    onClick: PropTypes.func,
    ele: PropTypes.shape({
            'id': PropTypes.number,
            'name': PropTypes.string,
            'description': PropTypes.string,
            'imgURL': PropTypes.string,
        })
}