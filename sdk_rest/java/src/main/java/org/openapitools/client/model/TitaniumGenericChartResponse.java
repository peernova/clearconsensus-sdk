/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.TitaniumColumnInfo;
import org.openapitools.client.model.TitaniumGenericChartResponseRow;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumGenericChartResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:36:13.498051Z[UTC]")
public class TitaniumGenericChartResponse {
  public static final String SERIALIZED_NAME_COLUMNS = "columns";
  @SerializedName(SERIALIZED_NAME_COLUMNS)
  private List<TitaniumColumnInfo> columns = null;

  public static final String SERIALIZED_NAME_ROWS = "rows";
  @SerializedName(SERIALIZED_NAME_ROWS)
  private List<TitaniumGenericChartResponseRow> rows = null;

  public static final String SERIALIZED_NAME_TOTAL_ROWS = "totalRows";
  @SerializedName(SERIALIZED_NAME_TOTAL_ROWS)
  private Integer totalRows;

  public TitaniumGenericChartResponse() { 
  }

  public TitaniumGenericChartResponse columns(List<TitaniumColumnInfo> columns) {
    
    this.columns = columns;
    return this;
  }

  public TitaniumGenericChartResponse addColumnsItem(TitaniumColumnInfo columnsItem) {
    if (this.columns == null) {
      this.columns = new ArrayList<>();
    }
    this.columns.add(columnsItem);
    return this;
  }

   /**
   * Get columns
   * @return columns
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumColumnInfo> getColumns() {
    return columns;
  }


  public void setColumns(List<TitaniumColumnInfo> columns) {
    this.columns = columns;
  }


  public TitaniumGenericChartResponse rows(List<TitaniumGenericChartResponseRow> rows) {
    
    this.rows = rows;
    return this;
  }

  public TitaniumGenericChartResponse addRowsItem(TitaniumGenericChartResponseRow rowsItem) {
    if (this.rows == null) {
      this.rows = new ArrayList<>();
    }
    this.rows.add(rowsItem);
    return this;
  }

   /**
   * Get rows
   * @return rows
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumGenericChartResponseRow> getRows() {
    return rows;
  }


  public void setRows(List<TitaniumGenericChartResponseRow> rows) {
    this.rows = rows;
  }


  public TitaniumGenericChartResponse totalRows(Integer totalRows) {
    
    this.totalRows = totalRows;
    return this;
  }

   /**
   * Get totalRows
   * @return totalRows
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getTotalRows() {
    return totalRows;
  }


  public void setTotalRows(Integer totalRows) {
    this.totalRows = totalRows;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumGenericChartResponse titaniumGenericChartResponse = (TitaniumGenericChartResponse) o;
    return Objects.equals(this.columns, titaniumGenericChartResponse.columns) &&
        Objects.equals(this.rows, titaniumGenericChartResponse.rows) &&
        Objects.equals(this.totalRows, titaniumGenericChartResponse.totalRows);
  }

  @Override
  public int hashCode() {
    return Objects.hash(columns, rows, totalRows);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumGenericChartResponse {\n");
    sb.append("    columns: ").append(toIndentedString(columns)).append("\n");
    sb.append("    rows: ").append(toIndentedString(rows)).append("\n");
    sb.append("    totalRows: ").append(toIndentedString(totalRows)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("columns");
    openapiFields.add("rows");
    openapiFields.add("totalRows");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumGenericChartResponse
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumGenericChartResponse.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumGenericChartResponse is not found in the empty JSON string", TitaniumGenericChartResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumGenericChartResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumGenericChartResponse` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      JsonArray jsonArraycolumns = jsonObj.getAsJsonArray("columns");
      if (jsonArraycolumns != null) {
        // ensure the json data is an array
        if (!jsonObj.get("columns").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `columns` to be an array in the JSON string but got `%s`", jsonObj.get("columns").toString()));
        }

        // validate the optional field `columns` (array)
        for (int i = 0; i < jsonArraycolumns.size(); i++) {
          TitaniumColumnInfo.validateJsonObject(jsonArraycolumns.get(i).getAsJsonObject());
        };
      }
      JsonArray jsonArrayrows = jsonObj.getAsJsonArray("rows");
      if (jsonArrayrows != null) {
        // ensure the json data is an array
        if (!jsonObj.get("rows").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `rows` to be an array in the JSON string but got `%s`", jsonObj.get("rows").toString()));
        }

        // validate the optional field `rows` (array)
        for (int i = 0; i < jsonArrayrows.size(); i++) {
          TitaniumGenericChartResponseRow.validateJsonObject(jsonArrayrows.get(i).getAsJsonObject());
        };
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumGenericChartResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumGenericChartResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumGenericChartResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumGenericChartResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumGenericChartResponse>() {
           @Override
           public void write(JsonWriter out, TitaniumGenericChartResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumGenericChartResponse read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumGenericChartResponse given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumGenericChartResponse
  * @throws IOException if the JSON string is invalid with respect to TitaniumGenericChartResponse
  */
  public static TitaniumGenericChartResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumGenericChartResponse.class);
  }

 /**
  * Convert an instance of TitaniumGenericChartResponse to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

