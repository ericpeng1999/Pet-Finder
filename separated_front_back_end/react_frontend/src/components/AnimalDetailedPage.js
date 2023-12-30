import PropTypes from 'prop-types'

export const AnimalDetailedPage = ({animal, info, clicks}) => {
    console.log(animal)
    return(
        <div>
            <div><button onClick={()=>clicks[1](info['type'], info['page'])}>return</button></div>
            <div>{animal['name']}</div>
            <div>{JSON.stringify(animal, null, 0)}</div>
        </div>
    )
}

AnimalDetailedPage.propTypes = {
    animal: PropTypes.shape({
        'id': PropTypes.number,
        'name': PropTypes.string,
        'type': PropTypes.string,
        'page': PropTypes.number,
        'description': PropTypes.string,
        'smallImage': PropTypes.string,
        'fullImage': PropTypes.string,
    }),
    info: PropTypes.shape({
        'type': PropTypes.string,
        'page': PropTypes.number,
        'lastPage': PropTypes.number,
    }),
}