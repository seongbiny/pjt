# README

### UI 구성

1. **TodoTemplate** : 화면을 가운데에 정렬, 일정 관리를 보여준다. children으로 내부 JSX를 props로 받아와서 랜더링해 준다.
2. **TodoInsert** : 새로운 항목을 입력하고 추가할 수 있는 컴포넌트. state를 통해 인풋의 상태를 관리한다.
3. **TodoListItem** : 각 할 일 항목에 대한 정보를 보여준다. todo 객체를 props로 받아 와서 상태에 따라 다른 스타일의 UI를 보여준다.
4. **TodoList** : todos 배열을 props로 받아 온 후, 이를 배열 내장 함수 map을 사용해서 여러 개의 TodoListItem 컴포넌트로 변환하여 보여 준다.



```jsx
<TodoTemplate>
    <TodoInsert />
    <TodoList />
</TodoTemplate>
```



### App에서 todos 상태 사용하기

App에서 useState를 사용하여 todos라는 상태를 정의하고, todos를 TodoList의 props로 전달

```jsx
// App.js

import { useState } from 'react';

function App () {
    const [todos, setTodos] = useState([초기 데이터]);
    
    return (
      <TodoTemplate>
      <TodoInsert />
      <TodoList todos={todos} /> 
    </TodoTemplate>
    )
}

export default App;
```

TodoList에서 todos 값을 받아 온 후 TodoItem으로 변환하여 랜더링하도록 설정해야 한다.

```jsx
// TodoList.js

function TodoList ({ todos }){
    return (
        <div className="TodoList">
            {todos.map(todo =>(
                <TodoListItem todo={todo} key={todo.id} />
            ))}
        </div>
    )
}

export default TodoList;
```

props로 받아 온 todo 배열을 map을 통해 TodoListItem으로 이루어진 배열로 변환하여 랜더링해 주었다. todo 데이터는 통째로 props로 전달해 준다. 여러 종류의 값을 전달해야 하는 경우 객체로 통째로 전달하는 편이 나중에 성능 최적화를 할 때 편리하다.

TodoListItem 컴포넌트에서 받아 온 todo 값에 따라 제대로 된 UI를 보여줄 수 있도록 컴포넌트를 수정한다.

```jsx
// TodoListItem.js

...
function TodoListItem({ todo }){
    const { text, checked } = todo;
    
    return (
    <div className="TodoListItem">
            <div className={cn('checkbox', {checked})} onClick={() => onToggle(id)}>
                {checked ? <MdCheckBox /> : <MdCheckBoxOutlineBlank />}
                <div className="text">{text}</div>
            </div>
        </div>
    )
}

export default TodoListItem;
```

 ### Create

TodoInsert 컴포넌트에서 인풋 상태를 관리하고 App 컴포넌트에는 todos 배열에 새로운 객체를 추가하는 함수를 만들어 주어야 한다.

#### TodoInsert value 상태 관리하기

TodoInsert 컴포넌트에서 인풋에 입력하는 값을 관리할 수 있도록 useState를 사용하여 value라는 상태를 정의한다. 인풋에 넣어 줄 onChange 함수는 컴포넌트가 리랜더링될 때마다 함수를 새로 만드는 것이 아니라, 한 번 함수를 만들고 재사용할 수 있도록 useCallback Hook을 사용한다.

```jsx
// TodoInsert.js

...
function TodoInsert(){
    const [value, setValue] = useState('');
    const onChange = useCallback(e => {
        setValue(e.target.value);
    }, []);
    
    return (
    <form className="TodoInsert" onSubmit={onSubmit}>
	    <input 
              placeholder="할 일을 입력하세요"
              value={value}
              onChange={onChange}
            />
            <button type="submit">
                <MdAdd />
            </button>
        </form>
    )
}

export default TodoInsert;
```

#### todos 배열에 새 객체 추가하기

새로운 객체가 만들어질 때마다 id 값에 1씩 더해 주어야 한다. => useRef 사용. id 값을 랜더링되는 정보가 아니라 단순히 새 항목을 만들 때 참조되는 값일 뿐이니까

```jsx
// App.js

function App(){
    ...
    const nextId = useRef(4);
    const onInsert = useCallback(
    text => {
        const todo = {
            id: nextId.current,
            text,
            checked: false,
        };
        setTodos(todos.concat(todo));
        nextId.current += 1;
    }, [todos],);
    
    return (
    ...
    <TodoInsert onInsert={onInsert} />
        ...
    )
}
```

#### TodoInsert에서 onSubmit 이벤트 설정하기

App에서 TodoInsert에 넣어 준 onInsert 함수에 현재 userState를 통해 관리하고 있는 value 값을 파라미처로 넣어서 호출한다.

onSubmit이라는 함수를 만들고 form의 onSubmit으로 설정

props로 받아 온 onInsert 함수에 현재 value 값을 파라미터로 넣어서 호출하고, 현재 value 값을 초기화한다.
