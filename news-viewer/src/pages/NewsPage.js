import Categories from '../components/Categories';
import NewsList from '../components/NewsList';

function NewsPage({ match }){
    const category = match.params.category || 'all';

    return (
        <>
            <Categories />
            <NewsList category={category} />
        </>
    );
};

export default NewsPage;